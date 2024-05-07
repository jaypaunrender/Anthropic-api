from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)

@app.route('/generate_response', methods=['POST'])
def generate_response():
    # Get data from request
    data = request.get_json()

    # Check if required data is present
    if 'api_key' not in data or 'system_prompt' not in data or 'model' not in data or 'messages' not in data:
        return jsonify({"error": "Missing required data"}), 400

    api_key = data['api_key']
    system_prompt = data['system_prompt']
    model = data['model']
    messages = data['messages']

    try:
        # Initialize Anthropics client
        client = anthropic.Client(api_key=api_key)

        # Generate response
        response = client.messages.create(
            model=model,
            system=system_prompt,
            messages=messages
        )

        # Return the generated response
        return jsonify({"response": response.message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
