from abc import ABCMeta, abstractmethod
import typing as T

class GraiaProtocol(metaclass=ABCMeta):
    """Graia Framework 对于类似 mirai-api-http, cqhttp 这样的具有不同请求版本或者是类似
    aiohttp, requests, httpx, urllib 这样的 http 请求事件的处理专用抽象类,
    旨在为现有项目提供更好的技术栈支持和对多种无头客户端通信实现的框架化支持.

    由于 Graia Framework 已经有内建的一个[事件系统](https://github.com/GraiaProject/BroadcastControl),
    而本系统基于 asyncio 开发, 所以你的部分方法需要使用 async 关键字创建特殊的协程方法.

    本抽象协议实现中, 并不强制依赖 BroadcastControl, 但你的实现中需要强依赖 BroadcastControl, 望周知.  
    若需要关于错误的规范, 参阅模块 `graia.protocol.core.exceptions`

    强制要求实现以下方法/静态方法/类方法/魔法方法, 使用 typing 提供类型指导:
        sync method __init__(self, session: Any)
          描述: 指示 Application 实例化中提供的 Session 的处理方式, 本方法实现要求
            你提供一个 Session 的处理方式, 且不强制对其进行约束.
          举例: 用于存储类似 mirai-api-http 中的 session_key, auth_key 等信息, 并用于后续请求.

        [sync/coroutine] method authenticate(self) -> bool
          描述: 同步异步皆可. 本方法主要用于由 Application 控制的, 根据 Session 中所包含信息,
            对无头客户端进行一个请求并判断 Session 是否有效/信息是否错误,
            请求成功返回 True, 请求失败抛出错误或返回 False.

        [sync/coroutine] method is_vaild(self) -> bool
          描述: 同步异步皆可. 本方法由 Application 定时调用, 用于判断连接是否正常, 成功返回 True,
            失败或连接失效则返回 False.

        [sync/coroutine] method release(self)
          描述: 同步异步皆可. 本方法由 Application 被终止或在整个程序被终止时发出,
            无论返回值如何, 原操作仍会执行.

        [sync/coroutine] method event_receiver() -> Union[Generator[BaseEvent], AsyncGenerator[BaseEvent]]:
          描述: 用于向内建事件系统生成事件实例.
    """
    session: T.Any

    @abstractmethod
    def __init__(self, session: T.Any):
        pass

    @abstractmethod
    def authenticate(self) -> bool:
        pass

    @abstractmethod
    def is_vaild(self) -> bool:
        pass

    @abstractmethod
    def release(self) -> T.Any:
        pass

    @abstractmethod
    def event_receiver(self) -> T.Union[T.Generator[T.Any], T.AsyncGenerator[T.Any]]:
        pass