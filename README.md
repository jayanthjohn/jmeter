# Fix QID 997044 – Upgrade vulnerable MathJax (CVE-2023-39663)
RUN pip install --upgrade nbclassic && \
    npm install mathjax@3.2.2 --registry=<your-internal-npm-url> --prefix /tmp/mathjax-fix && \
    cp -r /tmp/mathjax-fix/node_modules/mathjax/* \
       /opt/anaconda3/lib/python3.13/site-packages/nbclassic/static/components/MathJax/ && \
    rm -rf /tmp/mathjax-fix