package id.develo.capstoneproject.ui.report

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import id.develo.capstoneproject.R
import id.develo.capstoneproject.data.local.entity.ReportEntity
import id.develo.capstoneproject.databinding.ActivityReportBinding
import id.develo.capstoneproject.ui.main.MainActivity

class ReportActivity : AppCompatActivity() {

    private lateinit var viewModel: ReportViewModel
    private lateinit var binding: ActivityReportBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityReportBinding.inflate(layoutInflater)
        setContentView(binding.root)

        viewModel = ReportViewModel()

        viewModel.isLoading.observe(this, {
            binding.progressBar.visibility = if (it) View.VISIBLE else View.GONE
        })

        viewModel.listReport.observe(this, {
            val listReport = ArrayList<ReportEntity>()
            listReport.addAll(it)

            val reportAdapter = ReportAdapter(listReport)
            binding.recyclerView.setHasFixedSize(true)
            binding.recyclerView.adapter = reportAdapter
            binding.recyclerView.layoutManager = LinearLayoutManager(this)
        })

        binding.btnSend.setOnClickListener{
            Toast.makeText(this, "Data has been sent to JAKI!", Toast.LENGTH_SHORT).show()
            startActivity(Intent(this, MainActivity::class.java))
        }
    }
}