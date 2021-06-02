package id.develo.capstoneproject

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import com.bumptech.glide.Glide
import id.develo.capstoneproject.databinding.ActivityMainBinding
import id.develo.capstoneproject.ui.about.AboutActivity
import id.develo.capstoneproject.ui.authentication.AuthActivity
import id.develo.capstoneproject.utils.AppPreferences

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        startDriving()

        moveToAbout()

        Glide.with(this)
            .load(R.drawable.img_banner)
            .into(binding.imageView)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        val inflater: MenuInflater = menuInflater
        inflater.inflate(R.menu.main_menu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle item selection
        return when (item.itemId) {
            R.id.action_logout -> {
                logout()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun logout() {
        if (AppPreferences.isLogin) {
            AppPreferences.isLogin = false
            AppPreferences.uId = 0
            AppPreferences.email = ""
            AppPreferences.password = ""
        }
        Intent(this, AuthActivity::class.java).also {
            startActivity(it)
            finish()
        }
    }

    private fun startDriving() {
        binding.btnStart.setOnClickListener {
            // DO SOMETHING
        }
    }

    private fun moveToAbout() {
        binding.btnAbout.setOnClickListener {
            Intent(this, AboutActivity::class.java).also {
                startActivity(it)
            }
        }
    }
}