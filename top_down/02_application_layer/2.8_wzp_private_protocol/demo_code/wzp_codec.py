"""WZP (WanZhi Protocol) minimal pack/unpack — teaching demo."""

from __future__ import annotations


def wzp_pack(cmd: int, body_str: str) -> bytes:
    """Len(4B big-endian) + Cmd(1B) + Body(UTF-8). Len counts Cmd+Body only."""
    payload = bytes([cmd & 0xFF]) + body_str.encode("utf-8")
    return len(payload).to_bytes(4, byteorder="big") + payload


def wzp_unpack_payload(payload: bytes) -> tuple[int, dict[str, str]]:
    """Parse Cmd+Body bytes (after length header)."""
    if not payload:
        raise ValueError("empty payload")
    cmd = payload[0]
    body = payload[1:].decode("utf-8")
    kv: dict[str, str] = {}
    for item in body.split("|"):
        if "=" in item:
            k, v = item.split("=", 1)
            kv[k] = v
    return cmd, kv


def wzp_read_frame(sock) -> tuple[int, dict[str, str]]:
    """Read one WZP frame from a blocking TCP socket."""
    len_buf = _recv_exact(sock, 4)
    n = int.from_bytes(len_buf, byteorder="big")
    payload = _recv_exact(sock, n)
    return wzp_unpack_payload(payload)


def _recv_exact(sock, n: int) -> bytes:
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("connection closed while reading WZP frame")
        buf.extend(chunk)
    return bytes(buf)


if __name__ == "__main__":
    frame = wzp_pack(0x01, "uid=10086|username=WZP用户|pass=abc123")
    print("packed:", frame.hex())
    # skip 4-byte len for demo
    cmd, kv = wzp_unpack_payload(frame[4:])
    print("cmd:", hex(cmd), "kv:", kv)
