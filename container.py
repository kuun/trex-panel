from dependency_injector import containers, providers

from service.trex_service import TrexService


class Container(containers.DeclarativeContainer):
    trex_service = providers.Singleton(TrexService)