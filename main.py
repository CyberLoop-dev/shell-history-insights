#!/usr/bin/env python3
"""Summarize shell history without printing command arguments."""
from __future__ import annotations
import argparse, csv, datetime as dt, json, re, shlex, sys
from collections import Counter
from pathlib import Path
ZSH = re.compile(r"^:\\s+(\\d+):\\d+;")

def parse_history(text: str) -> list[tuple[str, int | None]]:
    events=[]; stamp=None
    for raw in text.splitlines():
        line=raw.rstrip("\\n")
        match=ZSH.match(line)
        if match:
            stamp=int(match.group(1)); line=line[match.end():]
        elif line.startswith("#") and line[1:].isdigit():
            stamp=int(line[1:]); continue
        if not line.strip() or line.lstrip().startswith("#"): continue
        try: words=shlex.split(line)
        except ValueError: stamp=None; continue
        if words: events.append((Path(words[0]).name, stamp))
        stamp=None
    return events

def build_report(events, limit=10):
    counts=Counter(name for name,_ in events); hours=Counter(); dated=0
    for _,stamp in events:
        if stamp is not None:
            try: hours[dt.datetime.fromtimestamp(stamp).hour]+=1; dated+=1
            except (OverflowError,OSError,ValueError): pass
    return {"commands_analyzed":len(events),"timestamp_coverage_percent":round(dated*100/len(events),1) if events else 0.0,
            "top_commands":[{"command":n,"count":c} for n,c in counts.most_common(limit)],
            "usage_by_hour":[{"hour":h,"count":hours[h]} for h in sorted(hours)]}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file",type=Path,default=Path.home()/".bash_history")
    ap.add_argument("--format",choices=("text","json","csv"),default="text")
    ap.add_argument("--limit",type=int,default=10); args=ap.parse_args()
    if args.limit<1: ap.error("--limit must be positive")
    try: text=args.file.expanduser().read_text(encoding="utf-8",errors="replace")
    except OSError as exc: print(f"error: {exc}",file=sys.stderr); return 2
    report=build_report(parse_history(text),args.limit)
    if args.format=="json": print(json.dumps(report,indent=2))
    elif args.format=="csv":
        w=csv.writer(sys.stdout); w.writerow(("command","count")); w.writerows((x["command"],x["count"]) for x in report["top_commands"])
    else:
        print("Shell History Insights")
        print(f"Commands analyzed: {report['commands_analyzed']}")
        print(f"Timestamp coverage: {report['timestamp_coverage_percent']}%")
        for i,x in enumerate(report["top_commands"],1): print(f"{i:>2}. {x['command']:<18} {x['count']}")
    return 0
if __name__=="__main__": raise SystemExit(main())
