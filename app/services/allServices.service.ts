import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class AllServicesService {
	// All the API URLs
	private statesUrl = 'api/states';
	private partiesUrl = 'api/parties';
	private candidatesUrl = 'api/candidates';
	private electionsUrl = 'api/elections';
	private stateDetailsUrl = 'api/state';
	private partyDetailsUrl = 'api/party';
	private candidateDetailsUrl = 'api/candidate';
	private electionDetailsUrl = 'api/election';
	private testOutputUrl = 'api/test';
	private imageUrl = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDnOT53CCV948mcKY6rawsUNAAZqOoRKFU&cx=002168208795225832214:dup1kwhfope&searchType=image&imgSize=medium&q=';
	private searchResultsAndURL = 'api/s_and?term=';
	private searchResultsOrURL = 'api/s_or?term=';

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
		var singleStateUrl = this.stateDetailsUrl + "/" + id;
		return this.http.get(singleStateUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getPartyDetails(id: number): Observable<any> {
		var singlePartyUrl = this.partyDetailsUrl + "/" + id;
		return this.http.get(singlePartyUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getCandidateDetails(id: number): Observable<any> {
		var singleCandidateUrl = this.candidateDetailsUrl + "/" + id;
		return this.http.get(singleCandidateUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getElectionDetails(id: number): Observable<any> {
		var singleElectionUrl = this.electionDetailsUrl + "/" + id;
		return this.http.get(singleElectionUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getTestOutput(): Observable<any> {
		return this.http.get(this.testOutputUrl)
				   .map(this.extractTestData)
				   .catch(this.handleError);
	}

	getImageData(query: string):  Observable<any> {
		var queryUrl = this.imageUrl + query;
		return this.http.get(queryUrl)
				   .map(this.extractData)
				   .catch(this.handleError);
	}

	getAllSearchResults(str: string, searchType : string): Observable<any> {
		var replaced : string;
		if(str != null){
			replaced = str.replace('/ /g','%20');
		}
		var searchURL : string;
		if(searchType === "AND"){
			searchURL = this.searchResultsAndURL + replaced;
			return this.http.get(searchURL)
					   .map(this.extractData)
					   .catch(this.handleError);
		}
		else{
			searchURL = this.searchResultsOrURL + replaced;
			return this.http.get(searchURL)
						   .map(this.extractData)
						   .catch(this.handleError);
		}
	}



	private extractData(res: Response) {
		let body = res.json();
		return body.objects || body || {};
	}

	private extractTestData(res: Response) {
		return res.text();
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