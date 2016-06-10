//
//  Entity.swift
//  TechCompanies
//
//  Created by Marine Dejean on 5/29/16.
//  Copyright © 2016 Marine. All rights reserved.
//

import Foundation

enum EntityType:String {
    case None
    case School
    case TechCompany
}

class Entity {
    private (set) var name:String
    private (set) var town:String
    private (set) var imageName:String
    private (set) var type:EntityType 
    
    init (name:String, imageName:String, town:String, type:EntityType = .None){
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
}