import glob
import subprocess
from pathlib import Path

files = glob.glob("../*.py")

for f in files:
   path = Path(f) 
   subprocess.call(f"memray run -o ./memray-{path.stem}.bin {f} ", shell=True)
   subprocess.call(f"memray table -o ./memray-table-{path.stem}.html ./memray-{path.stem}.bin", shell=True)
   subprocess.call(f"memray flamegraph -o ./memray-flamegraph-{path.stem}.html ./memray-{path.stem}.bin", shell=True)
   subprocess.call(f"pyinstrument -r html -o ./pyinstrument-{path.stem}.html {f}", shell=True)

