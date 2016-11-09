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
var StatesTableComponent = (function () {
    function StatesTableComponent(allServicesService) {
        this.allServicesService = allServicesService;
        this.title = "States";
    }
    StatesTableComponent.prototype.ngOnInit = function () {
        this.getAllStates();
    };
    StatesTableComponent.prototype.getAllStates = function () {
        var _this = this;
        this.allServicesService.getAllStates().subscribe(function (allStates) { return _this.data = allStates; }, function (error) { return _this.errorMessage = error; });
    };
    StatesTableComponent = __decorate([
        core_1.Component({
            selector: 'states-table',
            templateUrl: 'app/components/states_table/states_table.html',
            providers: [
                allServices_service_1.AllServicesService
            ]
        }), 
        __metadata('design:paramtypes', [allServices_service_1.AllServicesService])
    ], StatesTableComponent);
    return StatesTableComponent;
}());
exports.StatesTableComponent = StatesTableComponent;
//# sourceMappingURL=states_table.component.js.map