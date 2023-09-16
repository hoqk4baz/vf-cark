from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/gamification/getSquatMarketingProductStatus', methods=['GET'])
def get_status():
    response_data = {
        "success": True,
        "code": 202,
        "message": "Eligible",
        "isJourneyComplete": True,
        "wheelConfig": {
            "isYouth": True,
            "isBirthday": False,
            "isAnniversary": False,
            "wheelSlices": [
                {"name": "İnternet", "value": "1"},
                {"name": "Dakika", "value": "2"},
                {"name": "Çekiliş Yanımda", "value": "3"},
                {"name": "İnternet", "value": "4"},
                {"name": "Her Şey Yanımda", "value": "5"},
                {"name": "İndirim Çeki", "value": "6"},
                {"name": "İnternet", "value": "7"},
                {"name": "Sınırsız Paket", "value": "8"}
            ]
        },
        "isTermsAndConditionsRequired": False
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3131)
