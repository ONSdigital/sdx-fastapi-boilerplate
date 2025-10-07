from pathlib import Path

from app.routes import router
from app.settings import Settings
from sdx_base.run import run

async def dummy_tx_id_getter(request):
    return "NA"

if __name__ == '__main__':
    proj_root = Path(__file__).parent
    run(Settings, routers=[router], proj_root=proj_root, get_tx_id=dummy_tx_id_getter)
