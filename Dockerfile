FROM python:3.15-slim

LABEL org.opencontainers.image.source="https://github.com/HeechanKim-Lab/OSS_11"
LABEL org.opencontainers.image.description="AmpliconSight Workbench & Micro-Tom Rhizosphere Pipeline Container"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY amplicon_platform/ ./amplicon_platform/
COPY web/ ./web/
COPY tests/ ./tests/
COPY package.json index.js ./

EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request, json; res = json.loads(urllib.request.urlopen('http://127.0.0.1:8080/health.json').read()); assert res['status'] == 'UP'" || exit 1

CMD ["python3", "-m", "http.server", "8080", "--directory", "web"]
