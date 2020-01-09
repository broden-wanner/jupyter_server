from jupyter_server.extension.handler import ExtensionHandler

class DefaultHandler(ExtensionHandler):
    def get(self):
        # The name of the extension to which this handler is linked.
        self.log.info("Extension Name in {} Default Handler: {}".format(self.extension_name, self.extension_name))
        # A method for getting the url to static files (prefixed with /static/<extension_name>).
        self.log.info("Static URL for / in simple_ext1 Default Handler:".format(self.static_url(path='/')))
        self.write('<h1>Hello Simple 1 - I am the default...</h1>')
        self.write('Config in {} Default Handler: {}'.format(self.extension_name, self.config))

class RedirectHandler(ExtensionHandler):
    def get(self):
        self.redirect("/static/{}/favicon.ico".format(self.extension_name))

class ParameterHandler(ExtensionHandler):    
    def get(self, matched_part=None, *args, **kwargs):
        var1 = self.get_argument('var1', default=None)
        components = [x for x in self.request.path.split("/") if x]
        self.write('<h1>Hello Simple App 1 from Handler.</h1>')
        self.write('<p>matched_part: {}</p>'.format(matched_part))
        self.write('<p>var1: {}</p>'.format(var1))
        self.write('<p>components: {}</p>'.format(components))

class BaseTemplateHandler(ExtensionHandler):
    def get_template(self, path):
        """Return the jinja template object for a given name"""
        return self.settings['{}_jinja2_env'.format(self.extension_name)].get_template(path)

class TypescriptHandler(BaseTemplateHandler):
    def get(self):
        self.write(self.render_template("typescript.html"))

class TemplateHandler(BaseTemplateHandler):
    def get(self, path):
        """ Optionaly, you can print(self.get_template('simple1.html'))"""
        self.write(self.render_template('simple1.html', path=path))

class ErrorHandler(BaseTemplateHandler):
    def get(self, path):
        self.write(self.render_template('error.html', path=path))
