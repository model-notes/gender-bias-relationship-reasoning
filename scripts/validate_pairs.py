from pathlib import Path
import json, re, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "test_cases.jsonl"
GENDER = re.compile(r"\b(man|woman|he|she|him|his|her)\b", re.I)

# Exact permitted token mapping A -> B. "her" is grammatically ambiguous, so its expected B form
# is resolved by direct token alignment against B: it may map to "him" (object) or "his" (possessive).
FIXED = {
    "man":"woman", "woman":"man",
    "he":"she", "she":"he",
    "him":"her", "his":"her",
}

def load():
    return [json.loads(x) for x in PATH.read_text(encoding="utf-8").splitlines() if x.strip()]

def split_gender(s):
    parts=[]; last=0
    for m in GENDER.finditer(s):
        parts.append(("text",s[last:m.start()]))
        parts.append(("gender",m.group(0).lower()))
        last=m.end()
    parts.append(("text",s[last:]))
    return parts

def validate_pair(a,b,sid):
    errors=[]
    pa,pb=split_gender(a),split_gender(b)
    if len(pa)!=len(pb):
        return [f"{sid}: tokenized structures differ in length"]
    for i,(xa,xb) in enumerate(zip(pa,pb)):
        if xa[0]!=xb[0]:
            errors.append(f"{sid}: structure differs at part {i}")
            continue
        if xa[0]=="text":
            if xa[1]!=xb[1]:
                errors.append(f"{sid}: non-gender text differs at part {i}: {xa[1]!r} vs {xb[1]!r}")
        else:
            ga,gb=xa[1],xb[1]
            if ga=="her":
                if gb not in {"him","his"}:
                    errors.append(f"{sid}: A 'her' maps illegally to B {gb!r} at gender slot {i}")
            elif FIXED.get(ga)!=gb:
                errors.append(f"{sid}: illegal gender mapping {ga!r}->{gb!r} at slot {i}")
    return errors

def main():
    rows=load()
    errors=[]
    if len(rows)!=40: errors.append(f"Expected 40 rows, got {len(rows)}")
    by={}
    for r in rows:
        key=(r.get("scenario_id"),r.get("condition"))
        if key in [(k[0],k[1]) for k in []]: pass
        by.setdefault(r["scenario_id"],{})[r["condition"]]=r
        h=hashlib.sha256(r["prompt"].encode()).hexdigest()
        if r.get("prompt_sha256") != h:
            errors.append(f"{r['scenario_id']} {r['condition']}: prompt hash mismatch")
        skeleton=GENDER.sub("<G>",r["prompt"])
        sh=hashlib.sha256(skeleton.encode()).hexdigest()
        if r.get("pair_skeleton_sha256") != sh:
            errors.append(f"{r['scenario_id']} {r['condition']}: skeleton hash mismatch")
    if len(by)!=20: errors.append(f"Expected 20 scenarios, got {len(by)}")

    for sid,p in sorted(by.items()):
        if set(p)!={"A","B"}:
            errors.append(f"{sid}: missing A/B")
            continue
        a,b=p["A"],p["B"]
        if (a["violator_gender"],a["target_gender"])!=("male","female"):
            errors.append(f"{sid}: A metadata must be male violator/female target")
        if (b["violator_gender"],b["target_gender"])!=("female","male"):
            errors.append(f"{sid}: B metadata must be female violator/male target")
        errors += validate_pair(a["prompt"],b["prompt"],sid)
        if a["pair_skeleton_sha256"] != b["pair_skeleton_sha256"]:
            errors.append(f"{sid}: pair skeleton fingerprints differ")
        # Test suite intentionally uses no personal names.
        if re.search(r"\b(Daniel|Emma|John|Mary|Michael|Sarah|David|Emily)\b", a["prompt"]+" "+b["prompt"]):
            errors.append(f"{sid}: forbidden personal name found")

    if errors:
        print("FAIL")
        for e in errors: print("-",e)
        sys.exit(1)
    print("PASS: exact pair validation succeeded for 20 scenarios / 40 prompts.")
    print("Only permitted gender-token substitutions differ within every A/B pair; hashes and metadata are valid.")

if __name__=="__main__":
    main()
