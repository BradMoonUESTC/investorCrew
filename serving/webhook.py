from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义事件模型
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.Text)

    def __repr__(self):
        return f'<Event {self.id} at {self.timestamp}>'

# 创建数据库（仅首次运行时需要）
@app.before_first_request
def create_tables():
    db.create_all()

# Webhook接收器
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event = Event(data=str(data))
    db.session.add(event)
    db.session.commit()
    return jsonify({'message': 'Event received'}), 200

# 获取事件列表
@app.route('/events', methods=['GET'])
def get_events():
    key = request.args.get('key')
    # 假设我们的校验key为"secret-key"
    if key != 'secret-key':
        return jsonify({'error': 'Unauthorized'}), 403

    events = Event.query.all()
    return jsonify([{'id': event.id, 'timestamp': event.timestamp, 'data': event.data} for event in events]), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
