FROM python:3.12-slim
 
RUN apt update && apt install -y \
    rsync \
    openssh-client \
    tar
   
 
WORKDIR /app
 
COPY backup.py .
 
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD \
    rsync --version && ssh -o BatchMode=yes ${BACKUP_USER}@${BACKUP_HOST} exit || exit 1
 
CMD ["python", "backup.py"]