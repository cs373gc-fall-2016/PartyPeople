import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class AllServicesService {
	// All the API URLs
	private statesUrl = 'api/state';
	private partiesUrl = 'api/party';
	private candidatesUrl = 'api/candidate';
	private electionsUrl = 'api/election';

	constructor(private http: Http) {}

	getAllStates(): Observable<any> {
		return this.http.get(this.statesUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getAllParties(): Observable<any> {
		return this.http.get(this.partiesUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getAllCandidates(): Observable<any> {
		return this.http.get(this.candidatesUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getAllElections(): Observable<any> {
		return this.http.get(this.electionsUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getStateDetails(id: number): Observable<any> {
		var singleStateUrl = this.statesUrl + "/" + id;
		return this.http.get(singleStateUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getPartyDetails(id: number): Observable<any> {
		var singlePartyUrl = this.partiesUrl + "/" + id;
		return this.http.get(singlePartyUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getCandidateDetails(id: number): Observable<any> {
		var singleCandidateUrl = this.candidatesUrl + "/" + id;
		return this.http.get(singleCandidateUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getElectionDetails(id: number): Observable<any> {
		var singleElectionUrl = this.electionsUrl + "/" + id;
		return this.http.get(singleElectionUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}








	private extractData(res: Response) {
		let body = res.json();
		return body.data || {};
	}

	private handleError (error: Response | any) {
		let errMsg: string;
	    if (error instanceof Response) {
	      const body = error.json() || '';
	      const err = body.error || JSON.stringify(body);
	      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
	    } else {
	      errMsg = error.message ? error.message : error.toString();
	    }
	    console.error(errMsg);
	    return Observable.throw(errMsg);
	}
}