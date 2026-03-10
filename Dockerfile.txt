# Use a lightweight Python base
FROM python:3.11-slim

# Install the RunPod SDK
RUN pip install --no-cache-dir runpod

# Copy the handler into the container
COPY handler.py /handler.py

# Run the handler (the -u flag ensures logs are sent to RunPod immediately)
CMD [ "python", "-u", "/handler.py" ]
