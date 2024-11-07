from flask import Flask

from service.service_route import app


class SpeechApp(Flask):
    def __init__(self, import_name,
                 static_url_path=None,
                 static_folder='static',
                 static_host=None, host_matching=False,
                 subdomain_matching=False,
                 template_folder='templates',
                 instance_path=None,
                 instance_relative_config=False,
                 root_path=None):
        super(SpeechApp, self).__init__(import_name,
                                        static_url_path=static_url_path,
                                        static_folder=static_folder,
                                        static_host=static_host,
                                        host_matching=host_matching,
                                        subdomain_matching=subdomain_matching,
                                        template_folder=template_folder,
                                        instance_path=instance_path,
                                        instance_relative_config=instance_relative_config,
                                        root_path=root_path)

        self.app = {}
        self.register_blueprint(app)
