//
//  ViewController.swift
//  Tapper
//
//  Created by Marine Dejean on 5/25/16.
//  Copyright © 2016 Marine. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var taps_requested:Int? = 0
    var taps_Done: Int = 0
    
    
    @IBOutlet weak var image_tapper: UIImageView!
    
    @IBOutlet weak var button_play: UIButton!
    
    @IBOutlet weak var textfield_number: UITextField!
    
    @IBOutlet weak var button_coin: UIButton!
    
    @IBOutlet weak var label_taps: UILabel!
    
    
    @IBAction func clickPlayButton(sender: AnyObject) {
        if self.textfield_number != nil && self.textfield_number.text != ""  {
            print("Lets do", Int(self.textfield_number.text!)!,"Taps!")
            self.taps_requested = Int(self.textfield_number.text!)
            if self.taps_requested != nil {
                self.initGame()
            }
        }
    }
    
    @IBAction func clickCoinButton(sender: AnyObject) {
        self.taps_Done += 1
        self.updateTapsLabel()
        if self.taps_Done < self.taps_requested{}
        if self.taps_Done > self.taps_requested {
            //reset the game
            self.resetgame()
            
        }
        
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        //--set initial values & attributes
        self.resetgame()
        
    }
    
    func initGame() {
        self.taps_Done = 0
        self.updateTapsLabel()
        self.image_tapper.hidden = true
        self.textfield_number.hidden = true
        self.button_play.hidden = true
        
        self.button_coin.hidden = false
        self.label_taps.hidden = false
    }
    
    func updateTapsLabel() {
        self.label_taps.text = String(self.taps_Done) + " Taps!"
    }
    
    func resetgame() {
        self.taps_requested = 0
        self.textfield_number.text = ""
        self.updateTapsLabel()
        self.image_tapper.hidden = false
        self.textfield_number.hidden = false
        self.button_play.hidden = false
        
        self.button_coin.hidden = true
        self.label_taps.hidden = true
        
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

