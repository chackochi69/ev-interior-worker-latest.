import runpod

print("Worker booting...")

def handler(job):
    print("Job received:", job)

    return {
        "status": "worker running"
    }

runpod.serverless.start(
    {
        "handler": handler
    }
)
