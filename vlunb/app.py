from flask import Flask, request, render_template, render_template_string
import os, requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>VLUB Console</title>
      <style>
        body {
          margin: 0;
          padding: 5vh 5vw;
          background: black;
          overflow: hidden;
          color: white;
          font-family: monospace;
        }

        nav {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          background: #111;
          padding: 10px;
          z-index: 9999;
        }

        nav a {
          color: limegreen;
          margin: 0 10px;
          text-decoration: none;
          font-weight: bold;
        }

        * {
          box-sizing: border-box;
        }

        p {
          font-family: monospace;
          font-weight: bold;
          font-size: 4.1vh;
          margin: 0;
          padding: 0;
          line-height: 1;
          color: limegreen;
          text-shadow: 0px 0px 10px limegreen;
        }

        .msg {
          font-family: monospace;
          font-weight: bold;
          text-transform: uppercase;
          font-size: 5vh;
          padding-top: 5vh;
          background: red;
          box-shadow: 0 0 30px red;
          text-shadow: 0 0 20px white;
          color: white;
          width: 20vw;
          height: 15vh;
          position: absolute;
          left: 50%;
          margin-left: -10vw;
          top: 50%;
          margin-top: -5vh;
          text-align: center;
          min-width: 200px;
          animation-name: blink;
          animation-duration: 0.6s;
          animation-iteration-count: infinite;
          animation-direction: alternate;
          animation-timing-function: linear;
        }

        @keyframes blink {
          0% { opacity: 0; }
          100% { opacity: 1; }
        }
      </style>
    </head>
    <body>

      <nav>
        <a href="/">Home</a>
        <a href="/hello">XSS Test</a>
        <a href="/login">Login</a>
        <a href="/ping">Ping</a>
        <a href="/ssrf">SSRF</a>
        <a href="/admin">Admin</a>
        <a href="/hacked">Defaced</a>
      </nav>

      <div class="msg">Scanning</div>
      <div id="console" style="margin-top: 80px;"></div>

      <script>
        var intervalID = window.setInterval(updateScreen, 200);
        var c = document.getElementById("console");

        var txt = [
          "FORCE: XX0022. ENCYPT://000.222.2345",
          "TRYPASS: ********* AUTH CODE: ALPHA GAMMA: 1___ PRIORITY 1",
          "RETRY: REINDEER FLOTILLA",
          "Z:> /FALKEN/GAMES/TICTACTOE/ EXECUTE -PLAYERS 0",
          "================================================",
          "Priority 1 // local / scanning...",
          "scanning ports...",
          "BACKDOOR FOUND (23.45.23.12.00000000)",
          "BACKDOOR FOUND (13.66.23.12.00110000)",
          "BACKDOOR FOUND (13.66.23.12.00110044)",
          "...",
          "...",
          "BRUTE.EXE -r -z",
          "...locating vulnerabilities...",
          "...vulnerabilities found...",
          "MCP/> DEPLOY CLU",
          "SCAN: __ 0100.0000.0554.0080",
          "SCAN: __ 0020.0000.0553.0080",
          "SCAN: __ 0001.0000.0554.0550",
          "SCAN: __ 0012.0000.0553.0030",
          "SCAN: __ 0100.0000.0554.0080",
          "SCAN: __ 0020.0000.0553.0080"
        ];

        var docfrag = document.createDocumentFragment();

        function updateScreen() {
          txt.push(txt.shift());
          docfrag.textContent = '';  // Reset
          txt.forEach(function(e) {
            var p = document.createElement("p");
            p.textContent = e;
            docfrag.appendChild(p);
          });
          while (c.firstChild) {
            c.removeChild(c.firstChild);
          }
          c.appendChild(docfrag);
        }
      </script>

    </body>
    </html>
    '''

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>XSS Test</title>
    <style>
        body {{ background: black; color: limegreen; font-family: monospace; padding: 40px; }}
        a {{ color: red; text-decoration: none; font-weight: bold; }}
    </style>
    </head>
    <body>
    <h2>XSS Test Page</h2>
    <form method="get">
        <label>Enter Name (XSS vulnerable): </label>
        <input name="name" />
        <input type="submit" value="Greet" />
    </form>
    <p>Hello {name}</p>
    <br><a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    query = ""
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pass']
        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Login Test</title>
    <style>
        body {{ background: black; color: limegreen; font-family: monospace; padding: 40px; }}
        a {{ color: red; text-decoration: none; font-weight: bold; }}
    </style>
    </head>
    <body>
    <h2>Login Page (Simulated SQL Injection)</h2>
    <form method="post">
        Username: <input name="user"><br>
        Password: <input name="pass"><br>
        <input type="submit" value="Login">
    </form>
    <p>Executed Query:</p>
    <code>{query}</code>
    <br><br><a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/ping')
def ping():
    host = request.args.get('host', '')
    result = os.popen(f"ping -c 1 {host}").read() if host else ""
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Ping Test</title>
    <style>
        body {{ background: black; color: limegreen; font-family: monospace; padding: 40px; }}
        a {{ color: red; text-decoration: none; font-weight: bold; }}
    </style>
    </head>
    <body>
    <h2>Ping Host (Command Injection)</h2>
    <form method="get">
        Host: <input name="host">
        <input type="submit" value="Ping">
    </form>
    <pre>{result}</pre>
    <br><a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/ssrf')
def ssrf():
    url = request.args.get('url', '')
    result = ""
    try:
        if url:
            result = requests.get(url, timeout=2).text[:500]
    except:
        result = "Invalid URL or SSRF blocked"
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>SSRF Test</title>
    <style>
        body {{ background: black; color: limegreen; font-family: monospace; padding: 40px; }}
        a {{ color: red; text-decoration: none; font-weight: bold; }}
        textarea {{ width: 100%; height: 200px; background: #111; color: lime; padding: 10px; border: none; }}
    </style>
    </head>
    <body>
    <h2>SSRF Test Page</h2>
    <form method="get">
        URL to fetch: <input name="url" style="width:60%">
        <input type="submit" value="Fetch">
    </form>
    <br>
    <label>Response:</label>
    <textarea readonly>{result}</textarea>
    <br><a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/admin')
def admin():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Admin Page</title>
    <style>
        body {
            background: black;
            color: red;
            font-family: monospace;
            padding: 40px;
        }
        h2 {
            color: white;
        }
        .warning {
            background: red;
            color: black;
            padding: 10px;
            font-weight: bold;
            border: 2px solid white;
            text-align: center;
        }
        a {
            color: limegreen;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    </head>
    <body>
    <h2>⚠️ ADMIN PANEL ⚠️</h2>
    <div class="warning">Access Granted Without Authentication</div>
    <p>Welcome to the Admin Panel. This route is unprotected and demonstrates broken access control.</p>
    <br><a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/deface', methods=['POST'])
def deface():
    html = request.form.get('page', '<h1>Hacked!</h1>')
    with open("templates/hacked.html", "w") as f:
        f.write(html)
    return "Defaced"

@app.route('/hacked')
def hacked():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>System Hacked</title>
      <style>
        body {
          background: black;
          color: red;
          font-family: monospace;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
        }
        h1 {
          font-size: 7vh;
          text-shadow: 0 0 20px red;
          animation: flicker 1s infinite alternate;
        }
        p {
          font-size: 3vh;
          color: white;
          text-shadow: 0 0 10px red;
        }
        @keyframes flicker {
          from { opacity: 1; }
          to { opacity: 0.6; }
        }
        a {
          color: limegreen;
          margin-top: 20px;
          font-size: 2.5vh;
          text-decoration: none;
        }
      </style>
    </head>
    <body>
      <h1>💀 YOU'VE BEEN HACKED 💀</h1>
      <p>This page was defaced by VLUB. All systems compromised.</p>
      <a href="/">Return to Safety</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
