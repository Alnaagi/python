from flask import Flask, jsonify, request, send_from_directory
import sqlite3

app = Flask(__name__, static_folder="frontend")

# Query database for all rows or filtered rows
def query_db(search_term=""):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    query = """
        SELECT * FROM discovery_data
        WHERE mac_address LIKE ? OR 
              hostname LIKE ? OR 
              wmode LIKE ? OR 
              essid LIKE ? OR 
              product LIKE ? OR 
              fwversion LIKE ? OR 
              ip_address LIKE ?
    """
    wildcard_term = f"%{search_term}%"
    cursor.execute(query, (wildcard_term,) * 7)
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.get("q", "")  # Single search box
    results = query_db(search_term)
    
    return jsonify([
        {
            "essid": row[0],
            "fwversion": row[1],
            "hostname": row[2],
            "ip_address": row[3],
            "mac_address": row[4],
            "product": row[5],
            "source_url": row[6],
            "wmode": row[7],
        } for row in results
    ])
@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

if __name__ == "__main__":
    app.run(debug=True)
