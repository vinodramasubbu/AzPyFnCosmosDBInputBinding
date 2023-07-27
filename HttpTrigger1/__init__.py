import logging

import azure.functions as func


def main(req: func.HttpRequest, cosdbin: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #logging.info('Documents found: %s', len(cosdbin))
    #logging.info('First document: %s', cosdbin[0].to_json())
    #mydocs = {}
    #for doc in cosdbin:
    #    logging.info(doc.to_json())
    

    claimNumber = req.params.get('claimNumber')

    if not claimNumber:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            claimNumber = req_body.get('claimNumber')

    logging.info('First document: %s', claimNumber)
    logging.info('First document: %s', cosdbin[0].to_json())
    if claimNumber:
        return func.HttpResponse(cosdbin[0].to_json())
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a claimNumber in the query string or in the request body for a personalized response.",
             status_code=200
        )
