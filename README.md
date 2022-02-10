<html>
  </head>
  <body>
  <h2>ER4 DoS</h2>
  <p>ER4 birden fazla DoS saldırı çeşidini tek scriptte gerçekleştirmeyi amaçlayan bir test aracıdır.</p>
  <h2>Kullanım</h2>
    <p>Örnek kullanım[Udp flood] : python main.py -udp -t 192.168.1.1 -p 80 -d 200</p>
    <p>Örnek kullanım[Slowloris] : python main.py -sl -u hedefsite.com -p 80 -s 250</p>
    <table>
  <tr>
    <th>Parametre</th>
    <th>Açıklama</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>-h / --help</td>
    <td>Yardım menüsünü açar.</td>
    <td>Yok</td>
  </tr>
    <tr>
    <td>-udp / --udpflood</td>
    <td>Saldiri türü</td>
    <td>False</td>
  </tr>
  <tr>
    <td>-sl / --slowloris</td>
    <td>Saldiri türü</td>
    <td>False</td>
  </tr>
  <tr>
    <td>-u / --url</td>
    <td>Hedef URL adresi. Slowloris yöntemi kullanılacaksa girilmesi gerekir.</td>
    <td>Yok</td>
  </tr>
  <tr>
    <td>-t / --target</td>
    <td>Hedef IP adresi. Udp flood yöntemi kullanılacaksa girilmesi gerekir.</td>
    <td>Yok</td>
  </tr>
  <tr>
    <td>-p / --port</td>
    <td>Hedef port</td>
    <td>80</td>
  </tr>
  <tr>
    <td>-d / --duration</td>
    <td>Saldırı süresi. Udp flood yöntemi için girilmesi gerekir.</td>
    <td>100</td>
  </tr>
  <tr>
    <td>-s / --socket</td>
    <td>Açılacak soket miktarı. Slowloris yöntemi için girilmesi gerekir.</td>
    <td>100</td>
  </tr>
</table>
    </body>
</html>
