# Use AWS Lambda base image for Python 3.9
FROM public.ecr.aws/lambda/python:3.9

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy function code and model
COPY app.py ./

# Command for Lambda to run
CMD ["app.lambda_handler"]
