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
var ElectionsTableComponent = (function () {
    function ElectionsTableComponent(allServicesService) {
        this.allServicesService = allServicesService;
        this.title = "Elections";
        this.columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
        this.data = [
            { "STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps" },
            { "STATE NAME": "Colorado", "CAPITAL": "Denver", "POPULATION": "987654", "GOVERNOR": "asdfeqwrasdf", "PARTY IN CONTROL": "dems" },
            { "STATE NAME": "Arizona", "CAPITAL": "Phoenix", "POPULATION": "325478951", "GOVERNOR": "someone", "PARTY IN CONTROL": "who knows" }
        ];
    }
    ElectionsTableComponent.prototype.ngOnInit = function () {
        this.getAllElections();
    };
    ElectionsTableComponent.prototype.getAllElections = function () {
        var _this = this;
        this.allServicesService.getAllElections().subscribe(function (allElections) { return _this.data = allElections; }, function (error) { return _this.errorMessage = error; });
    };
    ElectionsTableComponent = __decorate([
        core_1.Component({
            selector: 'elections-table',
            templateUrl: 'app/components/elections_table/elections_table.html',
            providers: [
                allServices_service_1.AllServicesService
            ]
        }), 
        __metadata('design:paramtypes', [allServices_service_1.AllServicesService])
    ], ElectionsTableComponent);
    return ElectionsTableComponent;
}());
exports.ElectionsTableComponent = ElectionsTableComponent;
//# sourceMappingURL=elections_table.component.js.map