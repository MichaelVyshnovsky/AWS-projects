from flask import Flask, request, render_template, jsonify
import resource_s3 as resource_s3
import boto3

app = Flask(__name__)

BUCKET_NAME = "hw06-mdv21001"

def configure_routes(app):
    '''Setup all the API routes'''

    @app.route('/')
    def homepage():
        '''Show the main screen. This is the main entry point for the webapp'''
        return render_template("index.html")

    @app.route('/list_objects')
    def list_files():
        '''Return a JSON list of objects in the bucket'''
        files = resource_s3.list_contents(BUCKET_NAME)
        return jsonify(files)

    @app.route('/upload', methods=['POST'])
    def success():
        '''Process the file upload and return a success message'''
        if request.method == 'POST':
            file = request.files['file']
            result = resource_s3.upload(file, BUCKET_NAME)
            return jsonify(result)
        return jsonify({"message": "Operation not supported"}), 400

    @app.route('/get_thumbnail')
    def get_thumbnail():
        '''Return the image file from S3'''
        obj_name = request.args.get('obj')
        if not obj_name:
            return jsonify({"message": "Object name is required"}), 400

        s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=BUCKET_NAME, Key=obj_name)
            return response['Body'].read(), 200, {'Content-Type': response['ContentType']}
        except Exception as e:
            return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    configure_routes(app)
    app.run(host="0.0.0.0", port=5000)