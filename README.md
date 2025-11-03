# 🧹 Remove old JupyterLab 4.3.4 package remnants (to pass Qualys scan)
RUN find /opt/anaconda3/pkgs -type d -name "jupyterlab-4.3.4*" -exec rm -rf {} + \
    && find /opt/anaconda3/lib/python*/site-packages -type d -name "jupyterlab-4.3.4*" -exec rm -rf {} + \
    && echo "✅ Removed old JupyterLab 4.3.4 package remnants"

## Fix QID 997044 - Update vulnerable MathJax version
RUN pip install --upgrade nbclassic && \
    npm install mathjax@2.7.10 --prefix /tmp/mathjax-fix && \
    cp -r /tmp/mathjax-fix/node_modules/mathjax/* \
       /opt/anaconda3/lib/python3.13/site-packages/nbclassic/static/components/MathJax/ && \
    rm -rf /tmp/mathjax-fix