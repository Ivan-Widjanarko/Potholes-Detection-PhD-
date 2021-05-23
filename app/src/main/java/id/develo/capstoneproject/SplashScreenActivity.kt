package id.develo.capstoneproject

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.WindowManager
import id.develo.capstoneproject.ui.authentication.AuthActivity

@Suppress("DEPRECATION")
class SplashScreenActivity : AppCompatActivity() {

    private var SPLASH_TIME: Long = 2000

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash_screen)
        // Load splash screen then navigate to main activity after 2 seconds
        loadSplashScreen()
    }

    private fun loadSplashScreen() {
        // hide the status bar
        window.setFlags(
            WindowManager.LayoutParams.FLAG_FULLSCREEN,
            WindowManager.LayoutParams.FLAG_FULLSCREEN
        )

        Handler(Looper.getMainLooper()).postDelayed({
            Intent(this, AuthActivity::class.java).also {
                startActivity(it)
                finish()
            }
        }, SPLASH_TIME)
    }
}