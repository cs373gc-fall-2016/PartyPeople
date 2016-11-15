"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var http_1 = require('@angular/http');
var Observable_1 = require('rxjs/Observable');
require('rxjs/add/operator/map');
require('rxjs/add/operator/catch');
var AllServicesService = (function () {
    function AllServicesService(http) {
        this.http = http;
        // All the API URLs
        this.statesUrl = 'api/states';
        this.partiesUrl = 'api/parties';
        this.candidatesUrl = 'api/candidates';
        this.electionsUrl = 'api/elections';
        this.stateDetailsUrl = 'api/state';
        this.partyDetailsUrl = 'api/party';
        this.candidateDetailsUrl = 'api/candidate';
        this.electionDetailsUrl = 'api/election';
        this.testOutputUrl = '';
        this.imageUrl = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDnOT53CCV948mcKY6rawsUNAAZqOoRKFU&cx=002168208795225832214:dup1kwhfope&searchType=image&imgSize=medium&q=';
        this.searchResultsAndURL = 'api/s_and?term=';
        this.searchResultsOrURL = 'api/s_or?term=';
    }
    AllServicesService.prototype.getAllStates = function () {
        return this.http.get(this.statesUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getAllParties = function () {
        return this.http.get(this.partiesUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getAllCandidates = function () {
        return this.http.get(this.candidatesUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getAllElections = function () {
        return this.http.get(this.electionsUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getStateDetails = function (id) {
        var singleStateUrl = this.stateDetailsUrl + "/" + id;
        return this.http.get(singleStateUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getPartyDetails = function (id) {
        var singlePartyUrl = this.partyDetailsUrl + "/" + id;
        return this.http.get(singlePartyUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getCandidateDetails = function (id) {
        var singleCandidateUrl = this.candidateDetailsUrl + "/" + id;
        return this.http.get(singleCandidateUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getElectionDetails = function (id) {
        var singleElectionUrl = this.electionDetailsUrl + "/" + id;
        return this.http.get(singleElectionUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getTestOutput = function () {
        return this.http.get(this.testOutputUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getImageData = function (query) {
        var queryUrl = this.imageUrl + query;
        return this.http.get(queryUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getAllSearchResults = function (str, searchType) {
        var replaced = str.replace('/ /g', '%20');
        var searchURL;
        if (searchType === "AND") {
            searchURL = this.searchResultsAndURL + replaced;
            return this.http.get(searchURL)
                .map(this.extractData)
                .catch(this.handleError);
        }
        else {
            searchURL = this.searchResultsOrURL + replaced;
            return this.http.get(searchURL)
                .map(this.extractData)
                .catch(this.handleError);
        }
    };
    AllServicesService.prototype.extractData = function (res) {
        var body = res.json();
        console.log("Body: " + body);
        return body.objects || body || {};
    };
    AllServicesService.prototype.handleError = function (error) {
        var errMsg;
        if (error instanceof http_1.Response) {
            var body = error.json() || '';
            var err = body.error || JSON.stringify(body);
            errMsg = error.status + " - " + (error.statusText || '') + " " + err;
        }
        else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Observable_1.Observable.throw(errMsg);
    };
    AllServicesService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], AllServicesService);
    return AllServicesService;
}());
exports.AllServicesService = AllServicesService;
//# sourceMappingURL=allServices.service.js.map