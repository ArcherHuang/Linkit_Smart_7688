uci set wireless.sta.ssid="SSID"       # AP 的 SSID
uci set wireless.sta.key="KEY"         # AP 的 Password
uci set wireless.sta.encryption="psk"  # 加密模式
uci set wireless.sta.disabled="0"      # 開啟 Station Mode
uci commit
wifi