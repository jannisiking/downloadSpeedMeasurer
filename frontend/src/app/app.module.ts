import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppComponent} from './app.component';
import {HttpClientModule} from "@angular/common/http";
import {MeasurementsComponent} from './features/measurements/measurements/measurements.component';
import {
  MeasurementsListComponent
} from './features/measurements/measurements/measurements-list/measurements-list.component';
import {
  MeasurementsGraphComponent
} from './features/measurements/measurements/measurements-graph/measurements-graph.component';
import {MatTableModule} from "@angular/material/table";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatInputModule} from "@angular/material/input";
import {ReactiveFormsModule} from "@angular/forms";
import {MatButtonModule} from "@angular/material/button";

@NgModule({
  declarations: [
    AppComponent,
    MeasurementsComponent,
    MeasurementsListComponent,
    MeasurementsGraphComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserModule,
    BrowserAnimationsModule, // Erforderlich für Angular Material
    MatTableModule,
    MatInputModule,
    ReactiveFormsModule,
    MatButtonModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
