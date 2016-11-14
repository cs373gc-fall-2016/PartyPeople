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
var allServices_service_1 = require('../../services/allServices.service');
var CandidatesTableComponent = (function () {
    function CandidatesTableComponent(allServicesService) {
        this.allServicesService = allServicesService;
        this.title = "Candidates";
        this.loading = true;
    }
    CandidatesTableComponent.prototype.ngOnInit = function () {
        this.getAllCandidates();
    };
    CandidatesTableComponent.prototype.getAllCandidates = function () {
        var _this = this;
        this.allServicesService.getAllCandidates().subscribe(function (allCandidates) {
            _this.data = allCandidates;
            _this.loading = false;
        }, function (error) { return _this.errorMessage = error; });
    };
    CandidatesTableComponent = __decorate([
        core_1.Component({
            selector: 'candidates-table',
            templateUrl: 'app/components/candidates_table/candidates_table.html',
            providers: [
                allServices_service_1.AllServicesService
            ]
        }), 
        __metadata('design:paramtypes', [allServices_service_1.AllServicesService])
    ], CandidatesTableComponent);
    return CandidatesTableComponent;
}());
exports.CandidatesTableComponent = CandidatesTableComponent;
//# sourceMappingURL=candidates_table.component.js.map