# HeatpumpMonitor Documentation

## Local Preview

The docs can be built and previewed locally:

### 1. Clone repo and sub-modules 

    git clone https://github.com/openenergymonitor/heatpumpmonitor_docss

### 2. Install Sphinx

See: [http://www.sphinx-doc.org/en/master/usage/installation.html](http://www.sphinx-doc.org/en/master/usage/installation.html)

    pip3 install -U sphinx

### 3. Install The Theme

    pip3 install sphinx_rtd_theme

### 4. Install Plugins

    pip3 install m2r myst-parser sphinx_copybutton

### 5. Build and update the docs

Full update and re-build:

    ./update.sh
    
Re-build without update:

    ./make_clean_html.sh
    
Partial build:

    ./make_html.sh


This will generate html output in a `build` folder. The html can then be displayed using a local web server.

    sudo ln -sf /home/USERNAME/heatpumpmonitor_docs/main/_live /var/www/heatpumpmonitor_docs
