//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Marine Dejean on 5/29/16.
//  Copyright © 2016 Marine. All rights reserved.
//

import Foundation

class EntitiesHelper {
    
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    static func getSchools() -> [Entity]! {
        if listOfSchool.count == 0 {
            let Holberton = Entity(name: "Holberton", imageName: "Holberton",town: "San Francisco", type: .School)
            listOfSchool.append(Holberton)
        }
    return listOfSchool
}
        
    static func getTechCompanies() -> [Entity]! {
        if listOfTechCompany.count == 0 {
            listOfTechCompany.append(Entity(name: "Linkedin", imageName: "linkedin", town: "San Francisco", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", imageName: "docker", town: "San Francisco", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", imageName: "google", town: "Mountain View", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", imageName: "yahoo", town: "Sunnyvale", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", imageName: "apple", town: "Cupertino", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", imageName: "twitter", town: "San Francisco", type: .TechCompany))
        }
        // return list
        return listOfTechCompany
    }
}