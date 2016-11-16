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
var router_1 = require('@angular/router');
var allServices_service_1 = require('../../services/allServices.service');
var SearchResultsTableComponent = (function () {
    function SearchResultsTableComponent(route, allServicesService, router) {
        var _this = this;
        this.route = route;
        this.allServicesService = allServicesService;
        this.router = router;
        this.title = "Search Results";
        router.events.subscribe(function (val) {
            _this.ngOnInit();
        });
    }
    SearchResultsTableComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.route.queryParams.map(function (params) { return params['term']; }).subscribe(function (value) { return _this.searchTerm = value; });
        this.data = [];
        this.getAllSearchResults("AND");
    };
    SearchResultsTableComponent.prototype.getAllSearchResults = function (searchType) {
        var _this = this;
        this.allServicesService.getAllSearchResults(this.searchTerm, searchType).subscribe(function (allSearchResults) { return _this.data = allSearchResults; }, function (error) { return _this.errorMessage = error; });
    };
    SearchResultsTableComponent.prototype.andClicked = function () {
        document.getElementById("andButton").style.background = "#E0162B";
        document.getElementById("orButton").style.background = "#0052A5";
        this.getAllSearchResults("AND");
    };
    SearchResultsTableComponent.prototype.orClicked = function () {
        document.getElementById("andButton").style.background = "#0052A5";
        document.getElementById("orButton").style.background = "#E0162B";
        this.getAllSearchResults("OR");
    };
    SearchResultsTableComponent = __decorate([
        core_1.Component({
            selector: 'search-results-table',
            templateUrl: 'app/components/search_results_table/search_results_table.html',
            providers: [
                allServices_service_1.AllServicesService
            ],
            styles: [
                'app/components/search_results_table/search_results_table.css'
            ]
        }), 
        __metadata('design:paramtypes', [router_1.ActivatedRoute, allServices_service_1.AllServicesService, router_1.Router])
    ], SearchResultsTableComponent);
    return SearchResultsTableComponent;
}());
exports.SearchResultsTableComponent = SearchResultsTableComponent;
//# sourceMappingURL=search_results_table.component.js.map