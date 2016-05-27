//
//  File.swift
//  SimpleTableView
//
//  Created by Marine Dejean on 5/26/16.
//  Copyright © 2016 Marine. All rights reserved.
//

import Foundation

class TechCompaniesHelper {
    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
        static func getTechCompanies() -> [String] {
            return companies
        }
}