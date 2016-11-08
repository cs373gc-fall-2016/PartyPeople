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
        this.statesUrl = 'api/state';
        this.partiesUrl = 'api/party';
        this.candidatesUrl = 'api/candidate';
        this.electionsUrl = 'api/election';
        this.testOutputUrl = '';
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
        var singleStateUrl = this.statesUrl + "/" + id;
        return this.http.get(singleStateUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getPartyDetails = function (id) {
        var singlePartyUrl = this.partiesUrl + "/" + id;
        return this.http.get(singlePartyUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getCandidateDetails = function (id) {
        var singleCandidateUrl = this.candidatesUrl + "/" + id;
        return this.http.get(singleCandidateUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getElectionDetails = function (id) {
        var singleElectionUrl = this.electionsUrl + "/" + id;
        return this.http.get(singleElectionUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.getTestOutput = function () {
        return this.http.get(this.testOutputUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    AllServicesService.prototype.extractData = function (res) {
        var body = res.json();
        console.log("BODYYYYYYY: " + JSON.stringify(body));
        return body.objects || {};
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