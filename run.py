
from sdx_base.server.server import RouterConfig
from sdx_base.server.tx_id import txid_not_applicable

from app.routes import router
from app.settings import Settings, ROOT
from sdx_base.run import run


if __name__ == "__main__":

    routers = [RouterConfig(router=router, tx_id_getter=txid_not_applicable)]

    run(Settings, proj_root=ROOT, routers=routers)
