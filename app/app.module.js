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
var platform_browser_1 = require('@angular/platform-browser');
var router_1 = require('@angular/router');
var app_component_1 = require('./app.component');
var header_component_1 = require('./components/header/header.component');
var about_component_1 = require('./components/about/about.component');
var home_component_1 = require('./components/home/home.component');
var states_table_component_1 = require('./components/states_table/states_table.component');
var state_details_component_1 = require('./components/state_details/state_details.component');
var not_found_component_1 = require('./components/page_not_found/not_found.component');
var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        core_1.NgModule({
            imports: [
                platform_browser_1.BrowserModule,
                router_1.RouterModule.forRoot([
                    {
                        path: 'about',
                        component: about_component_1.AboutComponent
                    },
                    {
                        path: 'state/:id',
                        component: state_details_component_1.StateDetailsComponent
                    },
                    {
                        path: 'states',
                        component: states_table_component_1.StatesTableComponent
                    },
                    {
                        path: '',
                        component: home_component_1.HomeComponent
                    },
                    {
                        path: '**',
                        component: not_found_component_1.PageNotFoundComponent
                    }
                ])
            ],
            declarations: [
                app_component_1.AppComponent,
                header_component_1.HeaderComponent,
                about_component_1.AboutComponent,
                home_component_1.HomeComponent,
                states_table_component_1.StatesTableComponent,
                state_details_component_1.StateDetailsComponent,
                not_found_component_1.PageNotFoundComponent
            ],
            bootstrap: [app_component_1.AppComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], AppModule);
    return AppModule;
}());
exports.AppModule = AppModule;
//# sourceMappingURL=app.module.js.map