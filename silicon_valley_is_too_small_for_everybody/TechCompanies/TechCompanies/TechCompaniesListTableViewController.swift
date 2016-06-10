//
//  TechCompaniesListTableViewController.swift
//  TechCompanies
//
//  Created by Marine Dejean on 5/29/16.
//  Copyright © 2016 Marine. All rights reserved.
//
import UIKit

class TechCompaniesListTableViewController: UITableViewController {
    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    var sectionNames:[String] = ["Schools", "TechCompanies"]
    let techDetailSegue = "techDetailSegue"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        schoolList = EntitiesHelper.getSchools()
        techCompanyList = EntitiesHelper.getTechCompanies()
        
        self.title = "Schools & Tech Companies"
        
        /* var rightBarBtn = UIBarButtonItem(title: "Action", style: .plain, target: self, action: #selector(go))
         self.navigationController?.navigationItem*/
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false
        
        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: - Table view data source
    
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return sectionNames.count
    }
    
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return section == 0 ? schoolList.count : techCompanyList.count
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionNames[section]
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)
        
        // Configure the cell...
        if indexPath.section == 0 {
            //--SchoolList
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = " I love studying at  " + schoolList[indexPath.row].name
        }
            
        else {
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = " I love working at  " + techCompanyList[indexPath.row].name
            
        }
        return cell
    }
    
    /*
     // Override to support conditional editing of the table view.
     override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
     // Return false if you do not want the specified item to be editable.
     return true
     }
     */
    
    /*
     // Override to support editing the table view.
     override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
     if editingStyle == .Delete {
     // Delete the row from the data source
     tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
     } else if editingStyle == .Insert {
     // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
     }
     }
     */
    
    /*
     // Override to support rearranging the table view.
     override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {
     
     }
     */
    
    /*
     // Override to support conditional rearranging of the table view.
     override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
     // Return false if you do not want the item to be re-orderable.
     return true
     }
     */
    
    
    // MARK: - Navigation
    
    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        if segue.identifier == techDetailSegue {
            let indexPath = self.tableView.indexPathForCell(sender as! UITableViewCell)
            if let destinationViewController = segue.destinationViewController as? TechCompanyDetailViewController {
                // Pass the selected object to the new view controller.
                if indexPath!.section == 0 {
                    destinationViewController.entity = schoolList[indexPath!.row]
                    print(destinationViewController.entity.name)
                }
                else if indexPath!.section == 1 {
                    destinationViewController.entity = techCompanyList[indexPath!.row]
                }
            }
        }
    }
    
}