import json
from pathlib import Path
movies = [
    {"id":1,"name":"terminator"}
]
data = json.dumps(movies)
Path("z.json").write_text(data)
