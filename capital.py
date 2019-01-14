#
# This is a skeleton code for NUGU Play Backend server.
# This code can be executed on any Cloud Function, which allows us to implement backend serverless.
# Written by Seungho Han, SWE, SKKU.
# Contact: kevhahn97@skku.edu
#


class Response:
    def __init__(self, req):
        self.res = {'version': req['version']}
        self.res['resultCode'] = 'OK'
        self.res['output'] = {}

        # set your necessary utterance parameters to response
        self.set_parameters(
            {'country': req['action']['parameters']['country']['value']})

        # set your optional utterance parameters to response
        if req['action']['parameters'].get('YOUR_PARAMETER_NAME') != None:
            self.set_parameters(
                {'YOUR_PARAMETER_NAME': req['action']['parameters']['YOUR_PARAMETER_NAME']['value']})

    def set_parameters(self, key_values):
        self.res['output'].update(key_values)

    def make_response(self, req):
        # you can get your necessary parameters here
        country = req['action']['parameters']['country']['value']

        # you can get your optional parameters here
        if req['action']['parameters'].get('YOUR_PARAMETER_NAME') != None:
            parameter2 = req['action']['parameters']['YOUR_PARAMETER_NAME']['value']

        # do what you want
        # or add backend parameters here
        if country == '한국':
            capital = '서울'
            self.set_parameters({'capital': capital, 'isCapitalAvailable': 'yes'})
        else:
            self.set_parameters({'isCapitalAvailable': 'no'})


def main(args):
    response = Response(args)
    response.make_response(args)
    return response.res