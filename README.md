# 🧹 Remove old JupyterLab 4.3.4 package remnants (to pass Qualys scan)
RUN find /opt/anaconda3/pkgs -type d -name "jupyterlab-4.3.4*" -exec rm -rf {} + \
    && find /opt/anaconda3/lib/python*/site-packages -type d -name "jupyterlab-4.3.4*" -exec rm -rf {} + \
    && echo "✅ Removed old JupyterLab 4.3.4 package remnants"

# jmeter