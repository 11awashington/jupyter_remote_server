class NotebookSetting:
    def __init__(self, password, port):
        """ Initializes the notebook setting class
        :type password: Str
        :type port: Int
        """
        self.password = password
        self.port = port

    def setting(self, linux_user, ip):
        """ Creates the config data for the notebook
        :type linux_user: Str
        :rtype data: Str
        """
        data = "c = get_config()\n\
            c.IPKernelApp.pylab = 'inline'\n\
            c.NotebookApp.certfile = '/home/{0}/certs/mycert.pem'\n\
            c.NotebookApp.keyfile = '/home/{0}/certs/mykey.key'\n\
            c.NotebookApp.ip = \"{1}\"\n\
            c.NotebookApp.open_browser = False\n\
            c.NotebookApp.password = \"{2}\"\n\
            c.NotebookApp.port = {3}".format(linux_user, ip, self.password, self.port)

        return data.replace(" ", "")