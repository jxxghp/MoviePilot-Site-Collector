"""采集器测试网络隔离，不导入 MoviePilot 后端或访问真实站点。"""

import socket

import pytest
import requests
import websocket


@pytest.fixture(autouse=True)
def block_real_network(monkeypatch):
    """只允许测试桩完成 HTTP/CDP 交互，意外真实网络调用立即失败。"""
    def reject_network(*_arguments, **_keywords):
        """让缺少模拟的网络调用在测试中给出明确错误。"""
        raise AssertionError("采集器测试禁止真实网络，请模拟 HTTP/CDP 边界")

    monkeypatch.setattr(requests.sessions.Session, "request", reject_network)
    monkeypatch.setattr(websocket, "create_connection", reject_network)
    monkeypatch.setattr(socket, "create_connection", reject_network)
