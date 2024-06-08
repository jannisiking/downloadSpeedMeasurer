import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment";
import {Measurement} from "../model/measurement";
import {Observable, of} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  baseUrl = environment.base_url;

  constructor(
    private http: HttpClient
  ) { }

  getMeasurements(): Observable<Measurement[]>{
    return this.http.get<Measurement[]>(`${this.baseUrl}/data`);
  }
}
