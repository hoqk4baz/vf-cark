from flask import Flask, jsonify, request
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)

@app.route('/', defaults={'path': ''}, methods=['CONNECT','GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['CONNECT','GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def catch_all(path):
    # İstekin yapıldığı URL'yi alın
    request_url = request.url
    
    # Eğer istek URL'si /gamification/getSquatMarketingProductStatus içeriyorsa JSON yanıtını döndürün
    if '/gamification/getSquatMarketingProductStatus' in request_url:
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
    
    # Diğer URL'ler için hiçbir şey yapmayın (engelleme veya hata verme)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3131)
