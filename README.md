# Welcome to LinkIt Smart 7688 Duo

## Contents

- [Overview](#overview)
  - [物聯網架構與應用](#物聯網架構與應用)
  - [通訊協定與網路服務提供商](#通訊協定與網路服務提供商)
  - [實作架構](#實作架構)
- [檔案說明](#file-description)
- [開發板與感測器](#board-and-sensor)
  - [開發板](#開發板)
  - [擴充板](#擴充板)
  - [感測器](#感測器)
- [Pinout Diagram](#pinout-diagram)
- [IDE](#integrated-development-environment)
  - [Arduino](#arduino)
  - [Python](#python)
- [Arduino IDE 設定](#arduino-ide)
- [Firmware](#firmware)
- [Linkit Smart 7688 Duo Driver ( Windows Platform ) ](#linkit-smart-7688-duo-driver)
- [Library](#library)
  - [DHT](#dht)
  - [OLED](#oled)
- [Service](#service)
- [Firmware](#firmware)
- [Tools](#tools)
  - [Windows OS](#windows-os)
  - [macOS](#macos)
- [JSON Tools](#json-tools)
- [Troubleshooting](#troubleshooting)
- [Reference](#reference)
- [Blog](#blog)
- [License](#license)

## Overview       
[Back](#contents)

### 物聯網架構與應用                 
                                                                                                                                           
![Imgur](http://i.imgur.com/xLnaQpC.png)
                                  
### 通訊協定與網路服務提供商                 
                            
| 通訊協定 | 網路服務提供商 |
|---|---|
| HTTP | ThingSpeak、MediaTek Cloud Sandbox (MCS)、MediaTek Cloud Sandbox Lite (MCS Lite)、Google Firebase |
| MQTT | LASS、MediaTek Cloud Sandbox (MCS)、AWS IoT、IBM Bluemix IoT Platform |
| WebSocket | WoT.City |
                
### 實作架構
[Back](#contents)

![Imgur](http://i.imgur.com/WFNcC1p.png)
    
## File Description
[Back](#contents)

| 編號 | 資料夾 |  檔案名稱 | 說明  |
|---|---|---|---|
|1| /Basic  |  /ApMode_StationMode/apModeToStationMode.sh | 將 AP Mode 轉 Station Mode  |
|2| /Basic  |  /ApMode_StationMode/stationModeToApMode.sh | 將 Station Mode 轉 AP Mode  |
|3| /Basic  | /Get_MacAddress/Arduino/sketch_get_macAddress.ino  | 透過 Wi-Fi 按鈕取得 IP 或 Mac Address  |
|4| /IoT Cloud  |  /Arduino/getDHT/getDHT.ino | 取得 DHT 資料  |
|5| /IoT Cloud  |  /Arduino/DHT_OLED/DHT_OLED.ino |  將 DHT 資料顯示於 OLED |
|6| /IoT Cloud  |  /Arduino/getDUST/getDUST.ino |  取得 DUST 資料 |
|7| /IoT Cloud  |  /Arduino/DHT_DUST_OLED/DHT_DUST_OLED.ino |  將 DHT 與 DUST 資料顯示於 OLED |
|8| /IoT Cloud  |  /Arduino/getDHT_Bridge/getDHT_Bridge.ino |  將 DHT 的資料傳送到 MPU |
|9| /IoT Cloud  |  /Python/getSensorData.py | 從 MCU 取得 Sensor Data |
|10| /IoT Cloud  |  /Python/linkit_Smart_7688_MCS_MQTT.py | 將  Sensor Data 透過 MQTT 傳送到 MCS |
|11| /IoT Cloud  |  /Python/get_data_from_mcs_mqtt.py | 從 MCS 取得  Sensor Data |
|12| /IoT Cloud  |  /Python/linkit_Smart_7688_MCS.py | 將  Sensor Data 透過 API 傳送到 MCS |
|13| /IoT Cloud  |  /Python/linkit_Smart_7688_Thingspeak.py | 將  Sensor Data 傳送到 ThingSpeak |
|14| /IoT Cloud  |  /Python/linkit_Smart_7688_LASS.py | 將  Sensor Data 傳送到 LASS |
|15| /IoT Cloud  |  /Python/lass_to_thingspeak.py | 將 LASS 的資料傳送到 ThingSpeak |
|16| /IoT Cloud  |  /Python/linkit_Smart_7688_AWS_IoT.py | 將 Sensor Data 傳送到  AWS IoT |
|17| /IoT Cloud  |  /Python/linkit_Smart_7688_WoTCity.py | 將  Sensor Data 傳送到   WoT.City |
|18| /IoT Cloud  |  /Python/get_data_from_wot.py | 從 WoT.City 取得資料 |
|19| /IoT Cloud  |  /Python/linkit_Smart_7688_IBM_Bluemix_Publish.py | 將  Sensor Data 傳送到  IBM Bluemix |
|20| /IoT Cloud  |  /Python/linkit_Smart_7688_IBM_Bluemix_Subscribe.py | 從 IBM Bluemix 取得資料 |
|21| /IoT Cloud  |  /Python/linkit_Smart_7688_Firebase.py | 將  Sensor Data 傳送到 Google Firebase |

## Board and Sensor
[Back](#contents)

### 開發板
* [LinkIt Smart 7688 Duo](https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html)

### 擴充板
* [Arduino Breakout for LinkIt Smart 7688 Duo](https://www.seeedstudio.com/Arduino-Breakout-for-LinkIt-Smart-7688-Duo-p-2576.html)

### 感測器
* [Grove - Temperature & Humidity Sensor](https://www.seeedstudio.com/Grove-Temp%26Humi-Sensor-p-745.html)
* [Grove - Dust Sensor](https://www.seeedstudio.com/Grove-Dust-Sensor-p-1050.html)
* [Grove - OLED Display 1.12"](https://www.seeedstudio.com/Grove-OLED-Display-1.12%22-p-824.html)

## Pinout Diagram
[Back](#contents)

![Imgur](http://i.imgur.com/utzDNBs.png)

## Integrated Development Environment
[Back](#contents)

### Arduino
   *  [Arduino IDE v1.6.4](https://www.arduino.cc/en/Main/OldSoftwareReleases)
### Python
   * [Sublime Text](https://www.sublimetext.com/)
   * [Visual Studio Code](https://code.visualstudio.com/)
   * [Jupyter](http://jupyter.org/)   
      * 教學: [Link](http://oranwind.org/bid-data-mac-os-an-zhuang-jupyter/)
      * Command: ipython notebook
   * [IBM Data Science Experience Desktop](https://datascience.ibm.com/desktop) 

## Arduino IDE
[Back](#contents)

   *  ```檔案(File)``` ➙ ```偏好設定(Preferences)``` ➙ ```Additional Boards Manager URLs```
      http://download.labs.mediatek.com/package_mtk_linkit_smart_7688_test_index.json

## Firmware
[Back](#contents)

* [Download](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/downloads)

## Linkit Smart 7688 Duo Driver
[Back](#contents)

* [Download](http://download.labs.mediatek.com/mediatek_linkit_smart_7688_duo-windows-com-port-driver.zip )

## Library
[Back](#contents)

### DHT 
   * DHT sensor library by Adafruit Version: 1.2.3 )
     * 在 Arduino Sketch 中點選```草稿碼``` ➙ ```匯入程式庫``` ➙ ```管理程式庫``` ➙ 右上角搜尋欄位輸入 ```DHT``` ➙ 選擇 ```DHT sensor library by Adafruit Version: 1.2.3```

### OLED
   * Seeed OLED Display 128*64 library
     *  到 [Seeed OLED library Github](https://github.com/Seeed-Studio/OLED_Display_128X64) 頁面中的右上角下載整個 ZIP 檔
     *  在 Arduino Sketch 中點選```草稿碼``` ➙ ```匯入程式庫``` ➙ ```加入 .ZIP 程式庫```  ➙ 選擇上一步驟所下載的 ZIP 檔
      
## Service
[Back](#contents)

* [WoT.City](https://wotcity.com/)
* [Amazon Web Services Cloud](https://aws.amazon.com/tw/)
* [Google Firebase](https://firebase.google.com/)
* [IBM Bluemix](https://console.ng.bluemix.net/)
* [MediaTek Cloud Sandbox](https://mcs.mediatek.com)
* [ThingSpeak](https://thingspeak.com/)
* [ThinkSpeak Data Visualization](nrl.iis.sinica.edu.tw/LASS/PM25.php?site=III&city=台北市&district=信義區&channel=152239&apikey=9ND1FVDPKLQGPDRI)

## Firmware
[Back](#contents)

 * Linkit Smart 7688
   *  [Firmware](https://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/sdt_intro/index.gsp)

## Tools
[Back](#contents)

### Windows OS
   *  登入
      * Windows 端
        * [Putty](https://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)
   *  傳送檔案 
      * Windows 端
        * [FileZilla Client](https://filezilla-project.org/)
        * [WinSCP](https://winscp.net/eng/download.php)
      * Linkit Smart 7688 端 ( FileZilla Client )
        * ```opkg update```
        * ```opkg install openssh-sftp-server```   
### macOS
   *  登入 / 傳送檔案（本地端到 Linkit Smart 7688 端）- 終端機
      * 登入（在本地端電腦的終端機執行） ➙ ```ssh root@Linkit Smart 7688 的IP```
      * 傳送檔案（在本地端電腦的終端機執行） ➙ ```scp 在電腦中的檔案位置 root@Linkit Smart 7688 的IP:要傳送到 Linkit Smart 7688 中的位置```

## JSON Tools
[Back](#contents)

 * [JSON Lint](http://jsonlint.com/)
 * [JSON Editor Online](http://www.jsoneditoronline.org/)

## Troubleshooting
[Back](#contents)

 * 如果在瀏覽器輸入所設定的 local domain ( 預設為 ```http://mylinkit.local``` ) 後無法顯示設定頁時
   *  請安裝 [Bonjour Print Services](https://support.apple.com/kb/dl999?locale=zh_TW)
   *  再重新在瀏覽器輸入所設定的 local domain 
 * 當登入時發生 ```WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!``` 錯誤
   * 於終端機輸入 ```ssh-keygen -R IP位置 ```
   * 再重新 Login
  * COM Port 消失
   
    * [請參考教學文章](http://oranwind.org/-linkit-smart-7688-com-port-xiao-shi/)

## Reference
[Back](#contents)

* [Get Started with the LinkIt Smart 7688](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board)
* [Get Started with the LinkIt Smart 7688 Duo](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-duo-development-board)
* [LinkIt Smart 7688 Developer’s Guide](https://labs.mediatek.com/en/download/ih80Qtjo)

## Blog
[Back](#contents)

* [Archer @ 部落格](https://github.com/ArcherHuang/MyBlog/blob/master/README.md)

## License
[Back](#contents)

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

